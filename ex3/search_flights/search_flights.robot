*** Settings ***
Library         SearchFlightPage.py     Firefox    #Chrome
Suite Setup     Open
Suite Teardown  Close

*** Test Cases ***
The user can search for flights
    Select Departure City		Mexico City
    Select Destination City		London
    search_for_flights			
    @{flights}=	get_found_flights
    Should Not Be Empty     ${flights}
