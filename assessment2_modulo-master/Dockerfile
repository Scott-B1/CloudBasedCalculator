FROM ruby:2.7.2

RUN apt-get update -qq && apt-get install -y nodejs postgresql-client
RUN gem install rails bundler

COPY . .
RUN cd /modulo
WORKDIR /modulo

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update -qq && apt-get install -y yarn
RUN yarn install
RUN bundle update

EXPOSE 3000

CMD ["rails", "server", "-b", "0.0.0.0"]
