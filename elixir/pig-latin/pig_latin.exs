defmodule PigLatin do
  def translate(phrase) do
    Enum.join((for w <- String.split(phrase), do: convert(w)), " ")
  end

  defp convert(word) do
    cond do
      g = Regex.run(~r/^([aeiou]+|[x|y][^aeiou])(.*)/, word) ->
        "#{Enum.at(g, 1)}#{Enum.at(g, 2)}ay"
      g = Regex.run(~r/^(s?qu|[^aeiou]+)(.*)/, word) ->
        "#{Enum.at(g, 2)}#{Enum.at(g, 1)}ay"
    end
  end
end
