"""Implement POST request controller"""

from typing import Dict
from queries.estate_queries import GET_ESTATE


class GetEstateController:
    """
    Handle requests coming from /estate endpoint
    """
    @staticmethod
    def get_estate(
        db,
        request_params,
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
            query = db.query(GET_ESTATE)
        except Exception:
            return {"error": "error occurred while processing the request!"}
