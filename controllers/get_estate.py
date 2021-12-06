"""Implement POST request controller"""
import pandas as pd
from typing import Dict
from queries import estate_queries


class GetEstateController:
    """
    Handle requests coming from /estate endpoint
    """
    @staticmethod
    def get_estate(
        db,
        request_params: Dict,
    ) -> Dict:
        """get all estate 

        Parameters
        ----------
        db : DBConnection
            Singleton. controls connection to database
        request_params : dict
            a dictionary containing search parameters

        Returns
        -------
        Dict
            The response given by the controller
        """
        try:
            query = ""
            if "year" in request_params:
                year = request_params["year"]
                query = estate_queries.GET_ESTATE + f"AND YEAR >={year}"
            if "city" in request_params:
                city = request_params["city"]
                query = estate_queries.GET_ESTATE + f"AND CITY='{city}'"
            if "status" in request_params:
                status= request_params["status"]
                query = estate_queries.GET_ESTATE + f"AND STATUS ={status}"
            query = db.query(query)
                
        except Exception:
            return {"error": "error occurred while processing the request!"}
