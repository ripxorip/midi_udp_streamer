{
  description = "MIDI UDP streamer Python script";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        python = pkgs.python3;
        python-with-deps = python.withPackages (ps: [ ps.python-rtmidi ]);
      in {
        packages.default = pkgs.stdenv.mkDerivation {
          name = "midi-udp-streamer";
          src = ./.;
          buildInputs = [ python-with-deps ];
          installPhase = ''
            mkdir -p $out/bin
            cp stream_midi_udp.py $out/bin/stream_midi_udp.py
          '';
        };
        apps.default = {
          type = "app";
          program = "${python-with-deps.interpreter} ${self.packages.${system}.default}/bin/stream_midi_udp.py";
        };
        defaultPackage = self.packages.${system}.default;
        defaultApp = self.apps.${system}.default;
      }
    );
}
