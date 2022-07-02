import requests


class BitbucketApi:
    def __init__(self, access_token=None, refresh_token=None,
                 consumer_key=None, consumer_value=None, 
                 version=2):
        """
        :param access_token:
        :param refresh_token:
        :param consumer_key:
        :param consumer_value:
        :param version:
        """
        version = str(version)
        assert str(version) in '12', "Version should be 1 or 2 !"
        if version == '2':
            self.end_point = 'https://api.bitbucket.org/2.0'
        else:
            self.end_point = 'https://api.bitbucket.org/1.0'
        
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.consumer_key = consumer_key
        self.consumer_value = consumer_value
        self.version = version  

    def get_repo_from_workspace(self, workspace: str, repository_slug: str):
        """

        :param workspace: The workspace you want to get the repository from.
        :param repository_slug: The repository you want to retrieve from the workspace.
        :return: Repository Info.
        """
        url = f'{self.end_point}/repositories/{workspace}/{repository_slug}'
        authorization_token = f'Bearer <{self.access_token}>'
        response = requests.post(url, 
                                 headers={'Authorization': authorization_token})
        if response.status_code == 401:
            return {"error": "you are not authenticated or not authorized."}
        return response.json()
    
    def create_repo_in_workspace(self, workspace: str, repository_slug: str):
        """

        :param workspace: the workspace you want to create repo in.
        :param repository_slug: the repository slug.
        :return: response specify if the method is working.
        """
        url = f'{self.end_point}/repositories/{workspace}/{repository_slug}'
        authorization_token = f'Bearer <{self.access_token}>'
        response = requests.post(url, 
                                 headers={'Authorization': authorization_token})
        if response.status_code == 401:
            return {"error": "you are not authenticated or not authorized."}
        return response.json()

    def get_all_commits_in_repository(self, workspace: str, repository_slug: str, commit_hash: str):
        url = f'{self.end_point}/repositories/{workspace}/{repository_slug}/commit/{commit_hash}'
        authorization_token = f'Bearer <{self.access_token}>'
        response = requests.get(url, 
                                 headers={'Authorization': authorization_token})
        if response.status_code == 401:
            return {"error": "you are not authenticated or not authorized."}
        return response

    def delete_repo_in_workspace(self, workspace: str, repository_slug: str):
        
        url = f"{self.end_point}/repositories/{workspace}/{repository_slug}"
        authorization_token = f'Bearer <{self.access_token}>'
        response = requests.delete(url, headers={'Authorization': authorization_token})
        return response
    
    def get_all_repos_from_workspace(self, workspace: str):
        """

        :param workspace: The workspace you want to get the repositories from.
        :return: list of pages, for each page the repositories of it.
        """
        all_responses = []
        url = f'{self.end_point}/repositories/{workspace}'
        authorization_token = f'Bearer <{self.access_token}>'
        while True:
            response = requests.get(url, 
                                    headers={'Authorization': authorization_token})
            if response.status_code == 401: 
                return {"error": "you are not authenticated or not authorized"}
            data = response.json()
            all_responses.append(data)
            if 'next' not in data:
                break
            url = data['next']
        return all_responses
    
    def generate_access_token(self, code):
        """

        :param code: the code taken from here.
        :return: the new access token and other info.
        """
        assert (self.consumer_key is not None) and \
        (self.consumer_value is not None)
        url = f'{self.end_point}/site/oauth2/access_token'
        response = requests.post(url, data={'grant_type': 'authorization_code',
                                            'code': code},
                                 auth=(self.consumer_key, self.consumer_value))
        if response.status_code == 401:
            return {"error": "Not Authorized or Not Authenticated"}
        response = response.json()
        self.refresh_token = response['refresh_token']
        self.access_token = response['access_token']
        
        return response
        
    def refresh_access_token(self):
        """
        refresh the token.
        :return: None
        """
        assert (self.consumer_key is not None) and (self.consumer_value is not None)
        url = f'https://bitbucket.org/site/oauth2/access_token'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        response = requests.post(url,
                                 data={'grant_type': 'refresh_token',
                                       'refresh_token': self.refresh_token},
                                 auth=(self.consumer_key, self.consumer_value),
                                 headers=headers)
        if response.status_code == 401:
            return {"error": "Not Authorized or Not Authenticated"}
        response = response.json()
        self.access_token = response['access_token']
        self.refresh_token = response['refresh_token']
