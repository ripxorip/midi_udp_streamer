{
  description = "MIDI UDP streamer Python script";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        drv = import ./default.nix { inherit pkgs; };
      in {
        packages.default = drv;
        apps.default = {
          type = "app";
          program = "${drv}/bin/stream_midi_udp.py";
        };
        defaultPackage = drv;
        defaultApp = self.apps.${system}.default;
      }
    );
}
