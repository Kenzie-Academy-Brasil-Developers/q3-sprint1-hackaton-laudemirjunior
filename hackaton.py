def get_score(team_name, teams):
    result = 'Time não encontrado!'
    for index, team in enumerate(teams):
        if team == team_name:
            result = f'A {team_name} ficou classificada em {index+1}'  
    return result