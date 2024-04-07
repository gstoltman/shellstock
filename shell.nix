# shell.nix
let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      # select Python packages here
      python-pkgs.pandas
      python-pkgs.pyarrow
      python-pkgs.matplotlib
      python-pkgs.requests
      python-pkgs.pip
    ]))
  ];
}
