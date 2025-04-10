from agents import Agent, Runner
import asyncio

spanish_agent = Agent(
    name="Agente Español",
    instructions="Solo hablas en español.",
)

english_agent = Agent(
    name="Agente Inglés",
    instructions="Solo hablas en inglés",
)

triage_agent = Agent(
    name="Agente de Triage",
    instructions="Redirige al agente adecuado según el idioma de la solicitud.",
    handoffs=[spanish_agent, english_agent],
)


async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())