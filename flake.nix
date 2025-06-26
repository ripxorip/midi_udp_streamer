{
  description = "MIDI UDP streamer Python script";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python-with-deps = pkgs.python3.withPackages (ps: [ ps.python-rtmidi ]);
        drv = import ./default.nix { inherit pkgs; };
      in {
        packages.default = drv;
        apps.default = {
          type = "app";
          program = "${python-with-deps.interpreter} $out/bin/stream_midi_udp.py";
        };
        defaultPackage = drv;
        defaultApp = self.apps.${system}.default;
      }
    );
}
