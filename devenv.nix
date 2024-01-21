{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    version = "3.11";
    poetry = {
      enable = true;
      activate.enable = true;
    };
  };
  # See full reference at https://devenv.sh/reference/options/
}
