#!/bin/bash
set -e

INPUT_FILE="input.txt"

input=$(dagger query <<EOF | jq -r .host.directory.file.id
{
  host {
    directory(path:".") {
      file(path:"$INPUT_FILE") {
        id
      }
    }
  }
}
EOF
)

parser=$(dagger query <<EOF | jq -r .host.directory.file.id
{
  host {
    directory(path:".") {
      file(path:"parser.rs") {
        id
      }
    }
  }
}
EOF
)



answer=$(dagger query <<EOF | jq -r .container.from.withMountedFile.withMountedFile.withWorkdir.withExec.withExec.stdout
{
  container {
    from(address:"rust:latest") {
      withMountedFile(path:"/src/parser.rs", source:"$parser") {
        withMountedFile(path:"/input.txt", source:"$input") {
          withWorkdir(path:"/src") {
            withExec(args:["rustc","parser.rs"]) {
              withExec(args:["./parser"]) {
                stdout
              }
            }
          }
        }
      }
    }
  }
}
EOF
)

echo $answer