from models import Recipe, Chef
from main import Session


def create_recipe(name, ingredients, instructions):
    with Session() as session:
        new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        session.add(new_recipe)
        session.commit()
        return new_recipe


def update_recipe_by_name(name, new_name, new_ingredients, new_instructions):
    with Session() as session:
        recipe_to_update = session.query(Recipe).filter_by(name=name).first()
        if recipe_to_update:
            recipe_to_update.name = new_name
            recipe_to_update.ingredients = new_ingredients
            recipe_to_update.instructions = new_instructions
            session.commit()
        else:
            print('Recipe not found')


def delete_recipe_by_name(name):
    with Session() as session:
        recipe_to_delete = session.query(Recipe).filter_by(name=name).first()
        if recipe_to_delete:
            session.delete(recipe_to_delete)
            session.commit()
        else:
            print('Recipe not found')


def get_recipes_by_ingredient(ingredient_name):
    with Session() as session:
        recipes = session.query(Recipe).filter(Recipe.ingredients.contains(ingredient_name)).all()
        return recipes


def swap_recipe_ingredients_by_name(first_recipe_name, second_recipe_name):
    session = Session()
    transaction = session.begin()
    try:
        recipe1 = session.query(Recipe).filter_by(name=first_recipe_name).first()
        recipe2 = session.query(Recipe).filter_by(name=second_recipe_name).first()
        recipe1.ingredients, recipe2.ingredients = recipe2.ingredients, recipe1.ingredients
        transaction.commit()
    except Exception as e:
        transaction.rollback()
        raise e
    finally:
        session.close()


def relate_recipe_with_chef_by_name(recipe_name, chef_name):
    with Session() as session:
        recipe = session.query(Recipe).filter_by(name=recipe_name).first()
        if recipe and recipe.chef:
            raise Exception(f'Recipe: {recipe_name} already has a related chef')

        chef = session.query(Chef).filter_by(name=chef_name).first()
        recipe.chef = chef
        session.commit()
        return f'Related recipe {recipe_name} with chef {chef_name}'


def get_recipes_with_chef():
    with Session() as session:
        all_recipes = session.query(Recipe.name, Chef.name.label('chef_name')).join(Chef, Recipe.chef).all()

        return '\n'.join([f'Recipe: {recipe_name} made by chef: {chef_name}' for recipe_name, chef_name in all_recipes])

