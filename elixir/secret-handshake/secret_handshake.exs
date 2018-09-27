use Bitwise, only_operators: true


defmodule SecretHandshake do
  @actions ["wink", "double blink", "close your eyes", "jump"]
  def commands(code) do
    @actions
    |> Stream.with_index
    |> Stream.filter(fn {_, i} -> (1 <<< i &&& code) != 0 end)
    |> Stream.map(fn {e, _} -> e end)
    |> (&(if ((code &&& (1 <<< 4)) == 0), do: &1, else: Enum.reverse(&1))).()
    |> Enum.to_list
  end
end
