###Bitbucket API 

wrapper python code for using bitbucket api in easy way !

the code supports creating a repository inside a workspace,
 get repository from a workspace and listing all repositories from certain workspace.

 currently the Oauth2 works if you provide the key and then used generate_access_token.
 - you could generate a code from here
 https://developer.atlassian.com/cloud/bitbucket/rest/intro/#authentication
 on the Authorization Code Grant (4.1) Section

 also if you have the access token and the refresh token already, then you could use the system directly by specifying them. 