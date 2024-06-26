from contextlib import contextmanager

from diffusers.models.autoencoders.autoencoder_kl import AutoencoderKL
from diffusers.models.autoencoders.autoencoder_tiny import AutoencoderTiny


@contextmanager
def patch_vae_tiling_params(
    vae: AutoencoderKL | AutoencoderTiny,
    tile_sample_min_size: int,
    tile_latent_min_size: int,
    tile_overlap_factor: float,
):
    # Record initial config.
    orig_tile_sample_min_size = vae.tile_sample_min_size
    orig_tile_latent_min_size = vae.tile_latent_min_size
    orig_tile_overlap_factor = vae.tile_overlap_factor

    try:
        # Apply target config.
        vae.tile_sample_min_size = tile_sample_min_size
        vae.tile_latent_min_size = tile_latent_min_size
        vae.tile_overlap_factor = tile_overlap_factor
        yield
    finally:
        # Restore initial config.
        vae.tile_sample_min_size = orig_tile_sample_min_size
        vae.tile_latent_min_size = orig_tile_latent_min_size
        vae.tile_overlap_factor = orig_tile_overlap_factor
