import os
import boto3

class Config:
    def __init__(self):
        # Get API keys from AWS (we'll put them there securely)
        self.ssm = boto3.client('ssm', region_name='us-east-1')
    
    def get_secret(self, name):
        try:
            response = self.ssm.get_parameter(
                Name=f'/domain-bot/{name}',
                WithDecryption=True
            )
            return response['Parameter']['Value']
        except:
            return None
    
    @property
    def GODADDY_KEY(self):
        return self.get_secret('godaddy-key')
    
    @property  
    def GODADDY_SECRET(self):
        return self.get_secret('godaddy-secret')
    
    @property
    def NAMEJET_KEY(self):
        return self.get_secret('namejet-key')
    
    @property
    def FLIPPA_TOKEN(self):
        return self.get_secret('flippa-token')
    
    @property
    def SEMRUSH_KEY(self):
        return self.get_secret('semrush-key')
    
    # Robot settings - you can change these!
    MIN_TRAFFIC = 1000      # Only buy domains with 1000+ visitors/month
    MAX_BID = 50           # Never bid more than $50
    MIN_PROFIT = 3.0       # Only buy if we can make 3x our money