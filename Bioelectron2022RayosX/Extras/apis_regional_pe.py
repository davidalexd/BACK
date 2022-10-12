from typing import List, Optional
from .data_regional_pe import jsonDepartamentos,jsonDistritos,jsonProvincia
import requests
import json

class Regional:

    def get_departamentos(self) -> Optional[dict]:
        return jsonDepartamentos

    def get_distritos(self,dpt:str) -> Optional[dict]:
        return jsonDistritos[dpt]

    def get_provincia(self,dist:str) -> Optional[dict]:
        return jsonProvincia[dist]