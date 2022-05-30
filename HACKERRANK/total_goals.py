#!/bin/python3

import math
import os
import random
import re
import sys
from http.client import InvalidURL


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#


def getTotalGoals(team, year):
    # Write your code here
    page = 1
    try:
        team1_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
        team2_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"
        from urllib.request import Request, urlopen
        import json

        req1 = Request(team1_url)
        req2 = Request(team2_url)
        response1 = urlopen(req1)
        response2 = urlopen(req2)
        json1 = json.loads(response1.read().decode("utf-8"))
        json2 = json.loads(response2.read().decode("utf-8"))
        home_max_page = json1["total_pages"]
        away_max_page = json2["total_pages"]
        total_goals = 0
        for page in range(1, home_max_page + 1):
            team1_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
            response = urlopen(Request(team1_url))
            json_file = json.loads(response.read().decode("utf-8"))
            data = json_file["data"]
            for match in data:
                total_goals += int(match["team1goals"])
        for page in range(1, away_max_page + 1):
            team2_url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"
            response = urlopen(Request(team2_url))
            json_file = json.loads(response.read().decode("utf-8"))
            data = json_file["data"]
            for match in data:
                total_goals += int(match["team2goals"])
    except InvalidURL:
        total_goals = 0
    return total_goals


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + "\n")

    fptr.close()
