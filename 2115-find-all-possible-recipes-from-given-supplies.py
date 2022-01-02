class Solution:
    def findAllRecipes(
        self,
        recipes: List[str],
        ingredients: List[List[str]],
        supplies: List[str],
    ) -> List[str]:
        def is_recipe_reachable(i, seen):
            nonlocal reachable_recipes, unreachable_recipes, supplies, indices

            if i in seen:
                unreachable_recipes.add(i)
                return False

            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    if ingredient not in indices:
                        unreachable_recipes.add(i)
                        return False

                    j = indices[ingredient]
                    if j in unreachable_recipes:
                        unreachable_recipes.add(i)
                        return False

                    if not is_recipe_reachable(j, seen | {i}):
                        unreachable_recipes.add(i)
                        unreachable_recipes.add(j)
                        return False

            return True

        supplies = set(supplies)
        indices = {recipes[i]: i for i in range(len(recipes))}
        reachable_recipes = set()
        unreachable_recipes = set()
        for i in range(len(recipes)):
            if is_recipe_reachable(i, set()):
                reachable_recipes.add(i)

        return [recipes[i] for i in reachable_recipes]
