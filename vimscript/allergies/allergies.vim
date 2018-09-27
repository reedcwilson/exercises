
let s:allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
      \ 'chocolate', 'pollen', 'cats']

function! AllergicTo(score, allergy) abort
  return and(a:score, (float2nr(pow(2, index(s:allergies, a:allergy))))) > 0
endfunction

function! List(score) abort
  return filter(copy(s:allergies), {_, a -> AllergicTo(a:score, a)})
endfunction
