FROM ruby:2.6.0

# Install node
RUN apt update && apt install -y nodejs

# Install deps
WORKDIR /app
COPY Gemfile Gemfile.lock /app/
RUN bundle install

# Run migrations and precompilation
COPY . /app

ENV RAILS_ENV production
ENV RAILS_LOG_TO_STDOUT true

# Rails can read the SECRET_KEY_BASE from an env variable; no need to edit the encrypted file
ENV SECRET_KEY_BASE asdf

RUN rails db:migrate
RUN rake assets:precompile

# Run the app
EXPOSE 3000
ENTRYPOINT ["rails", "s"]
