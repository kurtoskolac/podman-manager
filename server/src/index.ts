import Fastify from 'fastify';

const fastify = Fastify({ logger: true });

// Basic route to check if our M4 is alive
fastify.get('/status', async (request, reply) => {
  return { 
    system: "Podman Manager", 
    status: "Active",
    platform: process.platform 
  };
});

const start = async () => {
  try {
    await fastify.listen({ port: 3000 });
    console.log('🚀 Server is running at http://localhost:3000');
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();
