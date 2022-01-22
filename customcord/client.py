from aiohttp import ClientSession
import logging

class Client:
    r"""Represents a client connection that connects to discord.
    This class is used to interact with the discord WebSocket and API.
    
    A number of options can be passed to the :class:`Client`.
    
    Parameters
    -----------
    token: str"""

    def __init__ (self, token: str):
        self.channels = []

        self.http = ClientSession(headers = {'Authorization': f'Bot {token}'}, base_url = 'https://discordapp.com/api/v9/')

        self.logs = open('logs.txt', 'w')
        self.logs.truncate(0)

    def send(self, method, **kwargs):
        r"""Sends a request to the discord API.
        
        Parameters
        ----------
        method: str
            The method to call.
        kwargs: dict
            The arguments to pass to the method.
        
        Returns
        -------
        :class:`RequestContextManager`
            The response from the API.
        """

        req = self.http.request('GET', f'/{method}', params = kwargs)
        self.logs.write(f'{req}\n')
        logging.DEBUG(f'{req}')
        return req
    
