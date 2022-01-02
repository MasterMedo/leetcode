class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        have = set(supplies)
        want = set(range(len(recipes)))
        need = set()
        made = []
        while len(need) != len(want):
            need = want.copy()
            for i in need:
                can_make = True
                for ingredient in ingredients[i]:
                    if ingredient not in have:
                        can_make = False
                        break

                if can_make:
                    made.append(recipes[i])
                    have.add(recipes[i])
                    want.remove(i)
        return made
