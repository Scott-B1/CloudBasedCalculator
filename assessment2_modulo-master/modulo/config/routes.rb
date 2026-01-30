Rails.application.routes.draw do
  root "modulo#new"

  get "/modulo", to: "modulo#new"
end
