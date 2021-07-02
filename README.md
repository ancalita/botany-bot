**Botany-bot** is a virtual assistant that helps you look after your houseplants!

It was built using [Rasa framework](https://rasa.com/docs/rasa/) (version 2.7) and it leverages the [knowledge base feature](https://rasa.com/docs/action-server/knowledge-bases).

The assistant can answer questions about water quantity, misting frequency and light amount for 8 different houseplants.
It can also provide an image for the requested plant, as well as answer what's the minimum temperature the plant can survive in.

Additionally, the assistant can also give advice on knowing when it's time to re-pot or water, as well as share instructions on how to re-pot your plant.

To run this bot on the CLI:
- make sure you have [installed](https://rasa.com/docs/rasa/installation/) Rasa Open Source
- train the bot: `rasa train`
- run the action server on a separate tab: `rasa run actions`
- run `rasa shell` to have a conversation with the bot
