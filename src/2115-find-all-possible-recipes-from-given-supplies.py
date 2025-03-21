class Solution:
    def findAllRecipes(
        self,
        recipes: list[str],
        ingredients: list[list[str]],
        supplies: list[str],
    ) -> list[str]:
        has_new_supplie = True
        recipes_created = []
        while has_new_supplie:
            if len(recipes_created) == len(recipes):
                break
            has_new_supplie = False
            for index, recipe in enumerate(recipes):
                has_all_ingredients_for_recipe = True
                for ingredient in ingredients[index]:
                    if ingredient not in supplies:
                        has_all_ingredients_for_recipe = False
                        break
                if (
                    has_all_ingredients_for_recipe
                    and recipe not in recipes_created
                ):
                    supplies.append(recipe)
                    has_new_supplie = True
                    recipes_created.append(recipe)
                    break
        return recipes_created


teste = Solution()
print(
    teste.findAllRecipes(
        recipes=["bread", "sandwich", "burger"],
        ingredients=[
            ["yeast", "flour"],
            ["bread", "meat"],
            ["sandwich", "meat", "bread"],
        ],
        supplies=["yeast", "flour", "meat"],
    )
)
