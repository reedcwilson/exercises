defmodule RotationalCipher do
  def rotate([], _shift), do: []

  def rotate([h|t], shift) when h in ?a..?z do
    [rotate_char(h, shift, ?a) | rotate(t, shift)]
  end

  def rotate([h|t], shift) when h in ?A..?Z do
    [rotate_char(h, shift, ?A) | rotate(t, shift)]
  end

  def rotate([h|t], shift), do: [h | rotate(t, shift)]

  def rotate(s, shift), do: rotate(to_charlist(s), shift) |> to_string

  defp rotate_char(c, shift, start), do: rem(c + shift - start, 26) + start
end
