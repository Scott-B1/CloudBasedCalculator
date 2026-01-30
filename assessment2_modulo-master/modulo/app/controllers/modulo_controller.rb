class ModuloController < ApplicationController
  def new
    x = params[:x].to_i
    y = params[:y].to_i
    if(y==0) #prevent error from divide/modulo by 0 exception
        answer=0
    else
      answer = x%y
    end

    render json:answer

  end
end
