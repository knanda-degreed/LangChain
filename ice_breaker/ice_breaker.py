import json

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
Sachin Ramesh Tendulkar, born 24 April 1973) is an Indian former international cricketer who captained the Indian national team.
 He is widely regarded as one of the greatest batsmen in the history of cricket. 
 He is the all-time highest run-scorer in both ODI and Test cricket with more than 18,000 runs and 15,000 runs, respectively.
 He also holds the record for receiving the most man-of-the-match awards in international cricket.
 Tendulkar was a Member of Parliament, Rajya Sabha by nomination from 2012 to 2018.
 Tendulkar took up cricket at the age of eleven, made his Test match debut on 15 November 1989 against Pakistan in Karachi at
  the age of sixteen, and went on to represent Mumbai domestically and India internationally for over 24 years.[9] In 2002, halfway through his career, Wisden ranked him the second-greatest Test batsman of all time, behind Don Bradman, and the second-greatest ODI batsman of all time, behind Viv Richards.[10] The same year, Tendulkar was a part of the team that was one of the joint-winners of the 2002 ICC Champions Trophy. Later in his career, Tendulkar was part of the Indian team that won the 2011 Cricket World Cup, his first win in six World Cup appearances for India.[11] He had previously been named "Player of the Tournament" at the 2003 World Cup.
 Tendulkar has received several awards from the government of India: the Arjuna Award (1994), the Khel Ratna Award (1997), the Padma Shri (1998), and the Padma Vibhushan (2008).[12][13] After Tendulkar played his last match in November 2013, the Prime Minister's Office announced the decision to award him the Bharat Ratna, India's highest civilian award.[14][15] He was the first sportsperson to receive the reward and, as of 2023, is the youngest recipient.[16][17][18] In 2010, Time included Tendulkar in its annual list of the most influential people in the world.[19] Tendulkar was awarded the Sir Garfield Sobers Trophy for cricketer of the year at the 2010 International Cricket Council (ICC) Awards.[20]

Having retired from ODI cricket in 2012,[21][22] he retired from all forms of cricket in November 2013 after playing his 200th Test match.[23] Tendulkar played 664 international cricket matches in total, scoring 34,357 runs.[24] In 2013, Tendulkar was included in an all-time Test World XI to mark the 150th anniversary of Wisden Cricketers' Almanack, and he was the only specialist batsman of the post–World War II era, along with Viv Richards, to get featured in the team.[25] In 2019, he was inducted into the ICC Cricket Hall of Fame.[26] On 24 April 2023, the Sydney Cricket Ground unveiled a set of gates named after Tendulkar and Brian Lara on the occasion of Tendulkar's 50th birthday and the 30th anniversary of Lara's inning of 277 at the ground.
"""


def summarise_information():
    summary_template = """
    Given the information {information} about a person, I want you to create:
    1. a short summary of their current state
    2. some interesting facts about them
    """
    summary_plus_prompt = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_plus_prompt)
    print(chain.run(information=information))


def summarise_linkedIn_information(json_data):
    summary_template = """
    Given the LinkedIn information {information} about a person, I want you to create:
    1. a short summary of their current state
    2. some interesting facts about them
    """
    summary_plus_prompt = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_plus_prompt)
    print(chain.run(information=json_data))


if __name__ == "__main__":
    print("Hello LangChain")

    # This is for the intro to langchain
    # summarise_information()

    # Summarise linkedIn profile of Colleagues
    json_file_path = "data/dblake.json"

    json_data = None

    try:
        with open(json_file_path, "r") as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        print(f"File on path {json_file_path} not found")
    except json.JSONDecodeError as e:
        print(f"Error decoding json {e}")

    if json_data is not None:
        print("JSON data successfully loaded")
        print(json_data)

    json_data = {
        k: v
        for k, v in json_data.items()
        if v not in ([], "", None)
        and k
        not in [
            "people_also_viewed",
            "groups",
            "similarly_named_profiles",
            "certifications",
        ]
    }

    print(f"Simplified JSON data is: {json_data}")

    summarise_linkedIn_information(json_data)

    # 1. Short Summary:
    # David Blake is the CEO and Executive Chairman at Degreed, a company focused on transforming the educational system. With a mission-driven approach, David aims to drive the cost of learning to zero, promote universal access to education, and establish meaningful indicators of educational outcomes and success. He has a diverse background in entrepreneurship, angel investing, and management consulting, and is actively involved in shaping the future of work, education, and politics.
    #
    # 2. Interesting Facts:
    # - David Blake co-founded Degreed in 2012 and has been instrumental in its growth and success. He has served as the CEO and Co-Founder, Executive Chairman, and currently holds the position of CEO and Executive Chairman.
    # - In addition to his role at Degreed, David is also the CEO and Co-Founder of BookClub, a company focused on reinventing book clubs for the digital age.
    # - David is a strong advocate for lifelong learning and believes in challenging people's worldview to foster empathy and personal growth.
    # - He has been an angel investor in various companies, including Sounding Board, Transfr VR, Prenda, Podium Education, and OnDeck. He also serves as an advisor to McKinsey & Co., GSV Ventures, and Firework Ventures.
    # - David has authored and co-authored several publications, including "The Expertise Economy" and "Jailbreaking the Degree," which explore the future of education and the need for innovative approaches.
    # - He holds a Bachelor's degree in Economics, Cum Laude, from Brigham Young University and has also completed the EdTech Entrepreneurs' Lab program at Hasso Plattner Institute, focusing on Design Thinking.
    # - David's passion for education and his dedication to creating meaningful change in the field have earned him a significant following, with over 16,000 followers on LinkedIn.
