const imports = [
    'bootstrap',
    'jquery'
]
const ready = ($) =>
{
    
}

require(imports,(bootstrap,$) => {
    $('document').ready(() => ready($))
})