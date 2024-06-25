const data = {{get_groups.data}}
let rv = []

for (let i=0; i<data.name.length; i++){
    let name = data.name[i]
    let id = data.id[i]
    rv.push{{name.id}}
}

return rv 
