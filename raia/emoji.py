# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 2024
Author: Alexandros Stratoudakis
e-mail: alexstrat4@gmail.com

"""
import warnings


emojis = {
    # emoji's definitions.
    "grinning_face": "\U0001F600",
    "grinning_face_with_big_eyes": "\U0001F603",
    "grinning_face_with_smiling_eyes": "\U0001F604",
    "beaming_face_with_smiling_eyes": "\U0001F601",
    "rolling_on_the_floor_laughing": "\U0001F923",
    "face_with_tears_of_joy": "\U0001F602",
    "slightly_smiling_face": "\U0001F642",
    "upside_down_face": "\U0001F643",
    "winking_face": "\U0001F609",
    "smiling_face_with_smiling_eyes": "\U0001F60A",
    "smiling_face_with_halo": "\U0001F607",
    "smiling_face_with_heart_eyes": "\U0001F60D",
    "star_struck": "\U0001F929",
    "face_blowing_a_kiss": "\U0001F618",
    "kissing_face": "\U0001F617",
    "kissing_face_with_squinting_eyes": "\U0001F61C",
    "kissing_face_with_closed_eyes": "\U0001F61A",
    "face_savoring_food": "\U0001F60B",
    "face_with_raised_eyebrow": "\U0001F928",
    "neutral_face": "\U0001F610",
    "expressionless_face": "\U0001F611",
    "unamused_face": "\U0001F612",
    "face_with_cold_sweat": "\U0001F613",
    "pensive_face": "\U0001F614",
    "worried_face": "\U0001F61F",
    "confused_face": "\U0001F615",
    "face_with_monocle": "\U0001F9D0",
    "nerd_face": "\U0001F913",
    "sunglasses": "\U0001F60E",
    "clown_face": "\U0001F921",
    "angry_face": "\U0001F620",
    "pouting_face": "\U0001F621",
    "face_with_symbols_on_mouth": "\U0001F92C",
    "exploding_head": "\U0001F92F",
    "flushed_face": "\U0001F633",
    "hot_face": "\U0001F975",
    "cold_face": "\U0001F976",
    "woozy_face": "\U0001F974",
    "sleeping_face": "\U0001F634",
    "drooling_face": "\U0001F924",
    "sleepy_face": "\U0001F60F",
    "face_with_thermometer": "\U0001F912",
    "face_with_head_bandage": "\U0001F915",
    "nauseated_face": "\U0001F922",
    "face_vomiting": "\U0001F92E",
    "sneezing_face": "\U0001F927",
    "face_with_cowboy_hat": "\U0001F920",
    "party_popper": "\U0001F389",
    "confetti_ball": "\U0001F38A",
    "tada": "\U0001F389",
    "balloon": "\U0001F388",
    "gift": "\U0001F381",
    "sparkles": "\U00002728",
    "fireworks": "\U0001F386",
    "sparkler": "\U0001F387",
    "christmas_tree": "\U0001F384",
    "snowman": "\U000026C4",
    "snowflake": "\U00002744",
    "mistletoe": "\U0001F338",
    "santa_claus": "\U0001F385",
    "sleigh": "\U0001F6F7",
    "jack_o_lantern": "\U0001F383",
    "spider": "\U0001F577",
    "spider_web": "\U0001F578",
    "skull": "\U0001F480",
    "ghost": "\U0001F47B",
    "alien": "\U0001F47D",
    "robot": "\U0001F916",
    "zombie": "\U0001F9DF",
    "money_mouth_face": "\U0001F911",
    "hugging_face": "\U0001F917",
    "smiling_face_with_sunglasses": "\U0001F60E",
    "face_with_hand_over_mouth": "\U0001F92D",
    "shushing_face": "\U0001F92B",
    "thinking_face": "\U0001F914",
    "loudly_crying_face": "\U0001F62D",
    "crying_face": "\U0001F622",
    "disappointed_face": "\U0001F61E",
    "fearful_face": "\U0001F628",
    "angry_face_with_horns": "\U0001F47F",
    "skull_and_crossbones": "\U00002620",
    "biohazard": "\U00002623",
    "radioactive_sign": "\U00002622",
    "warning": "\U000026A0",
    "stop_sign": "\U0001F6D1",
    "ballot_box_with_ballot": "\U0001F5F3",
    "wastebasket": "\U0001F5D1",
    "recycle": "\U00002702",
    "clinking_glasses": "\U0001F942",
    "beer_mug": "\U0001F37A",
    "tumbler_glass": "\U0001F943",
    "cup_with_straw": "\U0001F964",
    "bubble_tea": "\U0001F9CB",
    "coffee": "\U00002615",
    "tea": "\U0001F375",
    "chopsticks": "\U0001F962",
    "fork_and_knife": "\U0001F374",
    "plate_with_cutlery": "\U0001F37D",
    "spaghetti": "\U0001F35D",
    "hamburger": "\U0001F354",
    "fries": "\U0001F35F",
    "pizza": "\U0001F355",
    "taco": "\U0001F32E",
    "burrito": "\U0001F32F",
    "hotdog": "\U0001F32D",
    "popcorn": "\U0001F37F",
    "candy": "\U0001F36C",
    "lollipop": "\U0001F36D",
    "chocolate_bar": "\U0001F36B",
    "ice_cream": "\U0001F368",
    "shaved_ice": "\U0001F367",
    "birthday_cake": "\U0001F382",
    "cake": "\U0001F370",
    "cupcake": "\U0001F9C1",
    "doughnut": "\U0001F369",
    "cookie": "\U0001F36A",
    "milk": "\U0001F95B",
    "baby_bottle": "\U0001F37C",
    "bread": "\U0001F35E",
    "croissant": "\U0001F950",
    "baguette_bread": "\U0001F956",
    "cheese": "\U0001F9C0",
    "egg": "\U0001F95A",
    "peach": "\U0001F351",
    "cherry": "\U0001F352",
    "strawberry": "\U0001F353",
    "grapes": "\U0001F347",
    "melon": "\U0001F348",
    "watermelon": "\U0001F349",
    "banana": "\U0001F34C",
    "pineapple": "\U0001F34D",
    "apple": "\U0001F34E",
    "orange": "\U0001F34A",
    "lemon": "\U0001F34B",
    "pear": "\U0001F350",
    "avocado": "\U0001F951",
    "carrot": "\U0001F955",
    "corn": "\U0001F33D",
    "potato": "\U0001F954",
    "hot_pepper": "\U0001F336",
    "cucumber": "\U0001F952",
    "leafy_green": "\U0001F96C",
    "broccoli": "\U0001F966",
    "mushroom": "\U0001F344",
    "peanuts": "\U0001F95C",
    "chestnut": "\U0001F330",
    "basketball": "\U0001F3C0",
    "football": "\U0001F3C8",
    "soccer": "\U000026BD",
    "baseball": "\U000026BE",
    "tennis": "\U0001F3BE",
    "volleyball": "\U0001F3D0",
    "rugby_football": "\U0001F3C9",
    "bowling": "\U0001F3B3",
    "golf": "\U000026F3",
    "ping_pong": "\U0001F3D3",
    "badminton": "\U0001F3F8",
    "cricket_bat_and_ball": "\U0001F3CF",
    "field_hockey": "\U0001F3D1",
    "ice_hockey": "\U0001F3D2",
    "lacrosse": "\U0001F94D",
    "flying_disc": "\U0001F94F",
    "bow_and_arrow": "\U0001F3F9",
    "ski_and_snowboard": "\U0001F3C2",
    "skis": "\U0001F3BF",
    "snowboarder": "\U0001F3C2",
    "sled": "\U0001F6F7",
    "snowflake": "\U00002744",
    "sunny": "\U00002600",
    "cloud": "\U00002601",
    "rainbow": "\U0001F308",
    "thunder_cloud_and_rain": "\U000026C8",
    "lightning": "\U0001F4A5",
    "tornado": "\U0001F32A",
    "fog": "\U0001F32B",
    "wind_face": "\U0001F32C",
    "umbrella": "\U00002602",
    "high_voltage": "\U000026A1",
    "snowman": "\U000026C4",
    "snowman_without_snow": "\U0001F928",
    "sun_with_face": "\U0001F31E",
    "star": "\U00002B50",
    "star2": "\U0001F31F",
    "dizzy": "\U0001F4AB",
    "sparkles": "\U00002728",
    "fireworks": "\U0001F386",
    "sparkler": "\U0001F387",
    "balloon": "\U0001F388",
    "tada": "\U0001F389",
    "confetti_ball": "\U0001F38A",
    "party_popper": "\U0001F389",
    "ribbon": "\U0001F380",
    "gift": "\U0001F381",
    "christmas_tree": "\U0001F384",
    "tree": "\U0001F333",
    "deciduous_tree": "\U0001F333",
    "palm_tree": "\U0001F334",
    "cactus": "\U0001F335",
    "evergreen_tree": "\U0001F332",
    "tanabata_tree": "\U0001F38B",
    "bamboo": "\U0001F38D",
    "rock": "\U0001F5FF",
    "moon": "\U0001F314",
    "full_moon": "\U0001F315",
    "new_moon": "\U0001F311",
    "waxing_gibbous_moon": "\U0001F316",
    "waning_gibbous_moon": "\U0001F317",
    "first_quarter_moon": "\U0001F318",
    "last_quarter_moon": "\U0001F319",
    "moon_cake": "\U0001F96F",
    "sun": "\U0001F31E",
    "sunny": "\U00002600",
    "partly_sunny": "\U000026C5",
    "cloud_with_rain": "\U0001F327",
    "thunder_cloud_and_rain": "\U000026C8",
    "snowflake": "\U00002744",
    "snowman": "\U000026C4",
    "comet": "\U000026C4",
    "rainbow": "\U0001F308",
    "mountain_snow": "\U0001F3D4",
    "desert": "\U0001F3DC",
    "beach_umbrella": "\U0001F3D6",
    "umbrella_on_ground": "\U0001F5DD",
    "beach": "\U0001F3D6",
    "cityscape": "\U0001F3D9",
    "night_with_stars": "\U0001F303",
    "milky_way": "\U0001F30C",
    "stars": "\U0001F320",
    "maple_leaf": "\U0001F341",
    "fallen_leaf": "\U0001F342",
    "herb": "\U0001F33F",
    "four_leaf_clover": "\U0001F340",
    "shamrock": "\U0001F34B",
    "cherry_blossom": "\U0001F338",
    "white_flower": "\U0001F4AE",
    "bouquet": "\U0001F490",
    "rose": "\U0001F339",
    "wilted_flower": "\U0001F940",
    "sunflower": "\U0001F33B",
    "blossom": "\U0001F33C",
    "hibiscus": "\U0001F33A",
    "tulip": "\U0001F337",
    "seedling": "\U0001F331",
    "pineapple": "\U0001F34D",
    "banana": "\U0001F34C",
    "watermelon": "\U0001F349",
    "grapes": "\U0001F347",
    "strawberry": "\U0001F353",
    "cherry": "\U0001F352",
    "peach": "\U0001F351",
    "apple": "\U0001F34E",
    "orange": "\U0001F34A",
    "lemon": "\U0001F34B",
    "pear": "\U0001F350",
    "avocado": "\U0001F951",
    "carrot": "\U0001F955",
    "corn": "\U0001F33D",
    "potato": "\U0001F954",
    "red_heart": "\U0001F497",
    "orange_heart": "\U0001F9E1",
    "yellow_heart": "\U0001F49B",
    "green_heart": "\U0001F49A",
    "blue_heart": "\U0001F499",
    "purple_heart": "\U0001F49C",
    "brown_heart": "\U0001F90E",
    "black_heart": "\U0001F5A4",
    "white_heart": "\U0001F90D",
    "heart_on_fire": "\U0001F9E0",
    "sparkling_heart": "\U0001F496",
    "beating_heart": "\U0001F493",
    "two_hearts": "\U0001F495",
    "heart_with_arrow": "\U0001F498",
    "heart_with_ribbon": "\U0001F49D",
    "hand_with_index_finger_pointing_up": "\U000026D4",
    "thumbs_up": "\U0001F44D",
    "thumbs_down": "\U0001F44E",
    "ok_hand": "\U0001F44C",
    "victory_hand": "\U0000270C",
    "raised_hand": "\U0000270B",
    "clapping_hands": "\U0001F44F",
    "raising_hands": "\U0001F64C",
    "folded_hands": "\U0001F64F",
    "pray": "\U0001F64F",
    "muscle": "\U0001F4AA",
    "handshake": "\U0001F91D",
    "writing_hand": "\U0000270D",
    "point_right": "\U0001F449",
    "point_left": "\U0001F448",
    "point_up": "\U00002651",
    "point_down": "\U0001F447",
    "backhand_index_pointing_left": "\U0001F448",
    "backhand_index_pointing_right": "\U0001F449",
    "backhand_index_pointing_up": "\U0001F446",
    "backhand_index_pointing_down": "\U0001F447",
    "raised_back_of_hand": "\U0001F91A",
    "writing_hand": "\U0000270D",
    "pinching_hand": "\U0001F90F",
    "vulcan_salute": "\U0001F596",
    "ok_hand_sign": "\U0001F44C",
    "not_allowed": "\U000026D4",
    "raised_fist": "\U0000270A",
    "raised_hand_with_fingers_splayed": "\U0001F590",
    "hand_with_index_finger_and_thumb_crossed": "\U0001F91E",
    "call_me_hand": "\U0001F919",
    "ok_hand_sign": "\U0001F44C",

    # some codes from text
    ":)": "\U0001F642",          # Smiling face
    ":(": "\U0001F641",          # Frowning face
    ":D": "\U0001F603",          # Grinning face with big eyes
    ";)": "\U0001F609",          # Winking face
    ":P": "\U0001F61B",          # Face with stuck-out tongue
    ":'(": "\U0001F622",         # Crying face
    ":O": "\U0001F62E",          # Face with open mouth
    ":*": "\U0001F618",          # Face blowing a kiss
    "<3": "\U00002764",          # Heart
    "</3": "\U0001F494",         # Broken heart
    ":|": "\U0001F610",          # Neutral face
    ":/": "\U0001F615",          # Confused face
    "xD": "\U0001F606",          # Laughing face with squinting eyes
    ":@": "\U0001F620",          # Angry face
    "B)": "\U0001F60E",          # Smiling face with sunglasses
    ":3": "\U0001F617",          # Kissing face
    "o_O": "\U0001F632",         # Astonished face
    ":$": "\U0001F633",          # Flushed face
    ">:(": "\U0001F621",         # Pouting face
    "T_T": "\U0001F62D",         # Loudly crying face
    ":')": "\U0001F602",         # Face with tears of joy
    ":s": "\U0001F615",          # Confused face
    "8)": "\U0001F60E",          # Smiling face with sunglasses
    "<(": "\U0001F447",         # Backhand index pointing down
    "8|": "\U0001F632",          # Astonished face
}


class Emoji(object):
    """ Class that represents an emoji or a string of emojis"""

    def __init__(self, *args: str):
        """
        Initializer of the Emoji class.

        Args:
            *args (str): Name or names of emojis as str. Valid names are in raia.emoji.emojis.keys(). Invalid input will raise a warning.

        Returns:
            None.

        """
        self.UNICODE = ''
        for emj in args:
            if emj not in emojis:
                warnings.warn(
                    emj +
                    ' is not a valid emoji key. This argument will be ignored. The valid keys are '
                    + str([*emojis]))
            else:
                self.UNICODE += emojis.get(emj, '')

    def __str__(self):
        """ To make str(Emoji()) return unicode."""
        return self.UNICODE

    def __add__(self, string):
        """to add directly to strings"""
        return str(self) + string

    def __radd__(self, string):
        """ to make addition to a string ascociative"""
        return string + str(self)


# what to include with * import of the file
__all__ = ['emojis', 'Emoji']
