"""Implement POST request controller"""
import pandas as pd
from typing import Dict, List
from queries import estate_queries


class GetEstateController:
    """
    Handle requests coming from /estate endpoint
    """
    @staticmethod
    def get_estate(
        db,
        request_params: Dict,
    ) -> List:
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
            query_str = estate_queries.GET_ESTATE
            if "year" in request_params:
                year = request_params["year"]
                query_str = query_str + f"\nAND year >={year}"
            if "city" in request_params:
                city = request_params["city"]
                query_str = query_str + f"\nAND city='{city}'"
            if "statuses" in request_params:
                l=request_params["statuses"]
                query_str = query_str + "\nAND status_id IN (" + (','.join([ f"{x}" for x in l])) + ")"
            query = db.query(query_str)
            print(query_str)

            df = pd.DataFrame(
                query,
                columns = [
                    "Address", "City", "Price", "Description", "Status"
                ]
            )

            return df.to_dict('records')
                
        except Exception:
            return {"error": "error occurred while processing the request!"}
