
### A class to represent the functions that Symantec User Services provides

# authenticateUserWithPush -- sends a Push to a user's phone
class SymantecUserServices:

    #we should have a helper function to randomly generate request ID's in the best fashion

    # for now, pass in the client and play with it. pass in other things like requestID and such to
    #      this class's member functions since those aren't static. The client MAY be static, so thats for now
    def __init__(self, client, onBehalfOfAccountId=None, iaInfo=True, includePushAttributes=True):
        self.client = client
        self.onBehalfOfAccountId = onBehalfOfAccountId
        self.iaInfo = iaInfo
        self.includePushAttributes = includePushAttributes
        self.response = None


    def __str__(self, requestId, userId):
        res = str(self.client.service.authenticateUserWithPush(requestId=requestId, userId=userId))
        return res

    ###  Call the client's authenticateUser function
    def authenticateUser(self, requestId, userId, otpAuthData=None, pin=None, authContext=None):
        res = self.client.service.authenticateUser(requestId=requestId, userId=userId, otpAuthData=otpAuthData, pin=pin)
        self.response = str(res)
        return self.response


    def authenticateCredentials(self, requestId, credentials, otpAuthData=None, activate=None):
        res = self.client.service.authenticateCredentials(requestId=requestId, credentials=credentials, otpAuthData=otpAuthData)
        self.response = str(res)
        print(self.response)
        pass

    ###  Call the client's authenticateUserWithPush function
    def authenticateUserWithPush(self, requestId, userId, pin=None, displayParams=None, requestParams=None, authContext=None):
        res = self.client.service.authenticateUserWithPush(requestId=requestId, userId=userId)
        self.response = str(res)
        print(self.response)
        pass


    def getFieldContent(self, fieldname):
        info_list = self.response.split('\n')
        for item in info_list:
            if fieldname in item:
                return item.split('=')[1][1:]