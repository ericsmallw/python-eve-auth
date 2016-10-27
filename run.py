import bcrypt
import eventhooks
from eve import Eve
from eve.auth import BasicAuth
from eve.auth import TokenAuth
from flask import request


class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        accounts = app.data.driver.db['accounts']
        lookup = {'username': username}
        account = accounts.find_one()
        if allowed_roles:
            lookup['role'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        is_valid_account = account and bcrypt.hashpw(password.encode('utf-8'), account['password']) == account['password']
        return is_valid_account


class BCryptTokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        accounts = app.data.driver.db['accounts']
        lookup = {'token': token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['role'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        return account

app = Eve()
app.on_insert_accounts += eventhooks.hash_pass_and_token

@app.route('/login', methods=['POST', ])
def do_login():
    # default error response
    response = {'error': 'Credentials are invalid'}
    # use Eve's own db driver; no additional connections/resources are used
    accounts = app.data.driver.db['accounts']
    account = accounts.find_one({'username': request.form['username']})
    if account and '_id' in accounts:
        supplied_pass = bcrypt.hashpw(request.form['password'].encode('utf-8'), accounts['password'])
        if supplied_pass == accounts['password']:
            del account['password']
            response = account

    return response


if __name__ == '__main__':
    app.run()
