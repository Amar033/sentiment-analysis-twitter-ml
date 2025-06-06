{ pkgs }:
pkgs.mkShell {
  buildInputs = [
    pkgs.python311Full
    pkgs.git
    pkgs.git-lfs
    pkgs.pipenv
  ];
}
