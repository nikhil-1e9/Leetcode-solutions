class Solution:
  """
  You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

  Return a list answer of size 2 where:
  
  answer[0] is a list of all players that have not lost any matches.
  answer[1] is a list of all players that have lost exactly one match.
  The values in the two lists should be returned in increasing order.
  
  Note:
  You should only consider the players that have played at least one match.
  The testcases will be generated such that no two matches will have the same outcome.
  """
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
      ## First solution with 2 separate dictionaries for winners and losers
        winners, losers = {}, {}
        for match in matches:
            winners[match[0]] = winners.get(match[0],0) + 1
            losers[match[1]] = losers.get(match[1],0) + 1
        win, lose = [], []
        for w in winners:
            if w not in losers:
                win.append(w)
        for l in losers:
            if losers[l] == 1:
                lose.append(l)
        win.sort()
        lose.sort()
        return [win, lose]

        ## Solution using only one dictionary 
        loss = dict()
        for winner, loser in matches:
            loss[loser] = loss.get(loser,0)+1
            if winner not in loss:
                loss[winner] = 0
            else: continue
            
        zeroLoss, oneLoss = [], []
        for l in sorted(loss):
            if loss[l] == 0:
                zeroLoss.append(l)
            elif loss[l] == 1:
                oneLoss.append(l)
        return [zeroLoss, oneLoss]
