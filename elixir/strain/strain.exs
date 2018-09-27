defmodule Strain do
  def keep(list, fun), do: for e <- list, fun.(e), do: e 

  def discard(list, fun), do: keep(list, &(!fun.(&1)))
end
