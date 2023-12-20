import { 
    ApolloClient,
    createHttpLink,
    InMemoryCache,
} from "@apollo/client/core";

const httpLink = createHttpLink({
    uri: "http://127.0.0.1:8000/graphql", // Port used by django backend
});

const cache = new InMemoryCache();

const apolloClient = new ApolloClient({
    link: httpLink,
    cache,
});

export default apolloClient;