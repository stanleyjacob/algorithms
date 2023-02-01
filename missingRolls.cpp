public vector<int> missingRolls(vector<int> rolls, int mean, int n) {
      int knownSum = 0;
      for (int roll : rolls)
          knownSum += roll;
      int unknownSum = (rolls.size() + n) * mean - knownSum;

      if (unknownSum < n || unknownSum > n*6)
          return new int[] {};

      vector<int> result (n);

      int avgValue = unknownSum / n;
      int offset = unknownSum % n;
      for (int i=0; i < n; i++) {
          result[i] = avgValue;
          if (offset > 0)
              result[i] += 1;
          offset--;
      }
      return result;
  }
