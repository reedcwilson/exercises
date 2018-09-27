defmodule NucleotideCount do
  @nucleotides [?A, ?C, ?G, ?T]

  def count(strand, nucleotide) do
    Enum.count(strand, fn(c) -> c == nucleotide end)
  end

  def histogram(strand) do
    Map.new(@nucleotides, fn (n) -> {n, count(strand, n)} end)
  end
end
