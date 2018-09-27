defmodule Test1 do
  def sum(list, acc \\ 0)
  def sum([head | tail], acc), do: sum(tail, head + acc)
  def sum([], acc), do: acc
end

defmodule Test do
  def sum(list), do: list |> Enum.reduce(&(&1 + &2))
end

IO.puts Test.sum([1, 2, 3, 4])
