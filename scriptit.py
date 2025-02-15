from openai import OpenAI

client = OpenAI(
    base_url='https://external.api.recraft.ai/v1',
    api_key='API_KEY',
)

response = client.images.generate(
    prompt='a sign post in a city clearly written: For all overnight jobs and nightshifts, check OvernightjobsHQ',
    style='digital_illustration',
)
print(response.data[0].url)
