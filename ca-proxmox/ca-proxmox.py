class CAProxmox:
    """class to create CA certificates"""

    def __init__(self, *args, **kwargs) -> None:
        """Initiliaze the ca class"""

        # load parameters
        self.URL = kwargs.get("url", None)
        self.API_TOKEN = kwargs.get("api_token", None) 
        self.private_key = kwargs.get("key-path", None)

        
        self.vm_running = False 
        
        


    def start_vm(self):
        """Starts proxmox container and returns status"""

        if not self.vm_running:
            return True 

        else: 
            return False 

    
        

