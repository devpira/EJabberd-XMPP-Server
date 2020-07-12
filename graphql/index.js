const { ApolloServer, gql } = require('apollo-server');

const typeDefs = gql`
 type Chat {
    chatting_to: String
    chat_messages: [ChatMessage]
  }

  type ChatMessage {
    type: String
    message: String
    timestamp: Int
    created_at: String
  }

  type Query {
    Chats(myJid: Int): [Chat]
  }
`;

const resolvers = {
    Query: {

        Chats: (parent, {myJid}, context) => {
            if (!context.isAuth) {
                return dataSource
            } else {
                return null
            }
        },
        user: (parent, { id }, context) => dataSource.filter((item) => item.id === id)[0],
    },

    User: {
        recognitions: user => recognitios.filter((item) => item.userid === user.id),
    }
};

const server = new ApolloServer({typeDefs, resolvers});

server.listen().then(({ url }) => {
    console.log(`🚀  Server ready at ${url}`);
});