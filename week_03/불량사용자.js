const getPermutations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, selectNumber - 1);
    const attached = permutations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });
  return results;
};

function isBannedId(userIdCombination, bannedId) {
  for (let i = 0; i < userIdCombination.length; i++) {
    if (userIdCombination[i].length != bannedId[i].length) {
      return false;
    }
    for (let j = 0; j < userIdCombination[i].length; j++) {
      if (bannedId[i][j] != "*" && userIdCombination[i][j] != bannedId[i][j]) {
        return false;
      }
    }
  }
  return true;
}

function solution(user_id, banned_id) {
  return new Set(
    getPermutations(user_id, banned_id.length)
      .filter((userIdCombination) => {
        return isBannedId(userIdCombination, banned_id);
      })
      .map((userIdCombination) => userIdCombination.sort().join())
  ).size;
}
