def tally(rows):
    FORMAT = "{0:<31}|{1:>3} |{2:>3} |{3:>3} |{4:>3} |{5:>3}"
    RESULT = {'win':'loss','draw':'draw','loss':'win'}
    TABLE={}

    def calansewer(team,result):
        table = TABLE.get(team,{'Team':team, 'MP':0, 'W':0, 'D':0, 'L':0, 'P':0})
        table['MP']+=1
        table['W']+= (result=='win')
        table['D']+= (result=='draw')
        table['L']+= (result=='loss')
        table['P']+= 3 * (result=='win') + (result=='draw')
        TABLE[team]=table

    for result in rows:
        teama,teamb,res = result.split(';')
        calansewer(teama,res)
        calansewer(teamb,RESULT[res])

      
    table = [FORMAT.format('Team','MP','W','D','L','P')]+\
            [ FORMAT.format(t['Team'],t['MP'],t['W'],t['D'],t['L'], t['P']) \
            for t in sorted(sorted(TABLE.values(), key=lambda s:s['Team']), key=lambda r:r['P'], reverse=True)]
    return table
