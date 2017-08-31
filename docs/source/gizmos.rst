Gizmos
=======

Chromatic Abberations
---------------------

.. py:function:: chromatic_abberations

    Simulate `chromatic abberation <https://en.wikipedia.org/wiki/Chromatic_aberration>`_ lens effects.

    The effect is masked by a built-in radial that can be adjusted in softness and scale in the ``Effect`` section of the UI. By default the mask will ensure that the effect is more pronounced towards the edges of the image than in the centre. This can be overridden by plugging in a custom mask and switching ``Effect > Use Mask Input`` on.

    The standard weights will produce magenta/green chromatic abberations but can be tweaked in the ``Advanced > Weights`` section of the UI.

    By default, the aspect ratio is ``1.0`` on all channels, this can be tweaked in the ``Advanced > Aspect Ratios`` section of the UI to get a horizontally/vertically "squished" effect.

    .. image:: images/chromatic_abberations.png


    Global:

    :param Amount: Overall strength of the effect, i.e. separation of RGB channels, default: ``0.003``
    :type Amount: float
    :param Mix: Mix or opacity value, default: ``1.0``
    :type Mix: float

    Switches:

    :param Preview_Effect: Display the effect only, default: ``False``
    :type Preview_Effect: bool
    :param Use_Mask_Input: Use node's mask input instead of built-in radial mask, default: ``False``
    :type Use_Mask_Input: bool

    Mask:

    :param Softness: Softness of falloff of built-in radial mask, default: ``1.0``
    :type Softness: float
    :param Scale: Scale of built-in radial mask, default: ``2.0``
    :type Scale: float

    Advanced > Weights:

    :param Weight_R: Relative strength of the effect on the R channel, default: ``2.5``
    :type Weight_R: float
    :param Weight_G: Relative strength of the effect on the G channel, default: ``1.5``
    :type Weight_G: float
    :param Weight_B: Relative strength of the effect on the B channel, default: ``2``
    :type Weight_B: float

    Advanced > Aspect Ratios:

    :param Aspect_R: Height/width ratio of the effect on the R channel, default: ``1.0``
    :type Aspect_R: float
    :param Aspect_G: Height/width ratio of the effect on the G channel, default: ``1.0``
    :type Aspect_G: float
    :param Aspect_B: Height/width ratio of the effect on the B channel, default: ``1.0``
    :type Aspect_B: float


    Effect example:

    .. image:: images/chromatic_abberations_result.png



Grade Layer
-----------

.. py:function:: grade_layer

    In multi-pass compositing, passes or layers are usually shuffled out, tweaked and re-combined to build the beauty render. For pre-comps or other simple composites however, this might be an overhead and the artist will work directly with the multichannel EXR beauty instead.

    This gizmos allows the grading of a specific pass/layer, e.g. Reflection, even if passes have not been shuffled out and the result is being re-composited correctly back into the main beauty. It mirrors the Nuke Grade node, the only addition being the ``Layer`` drop-down menu from which the artist can select the pass/layer to grade.

    .. image:: images/grade_layer.png


    Global:

    :param Layer: Pass/Layer to be graded and re-composited, default: ``rgb``
    :type Layer: str


Photoshop Curves
----------------

.. py:function:: photoshop_curves

    When co-working with stills retouching teams, mood frames and colour grades might have been done in Photoshop using curves. These curves were therefore applied in ``sRGB`` and not in ``linear`` colour space as compared to Nuke's built-in ``ColorLookup``.

    This gizmo wraps a standard Nuke ``ColorLookup`` and performs a ``Colorspace`` conversion to and from ``sRGB`` before and after so the ``ColorLookup`` works almost exactly like Photoshop Curves.

    .. image:: images/photoshop_curves.png


Refraction Diffusion
--------------------

.. py:function:: refraction_diffusion

    Calculation spectral light effects can be very expensive if calculated in a 3D renderer.

    This gimzo simulates a spectral "Refraction Diffusion" effect and requires three separate channels inputs:

    - Refraction RGB
    - Refraction/IOR vectors with a low IOR, default: ``1.0``
    - Refraction/IOR vectors with a higher (glass-like) IOR, default: ``1.5``

    The Refraction/IOR vector passes can be rendered as a V-Ray SamplerInfo Render Element as described below. Adjust the ``Refract IOR`` value for each of the Refraction/IOR vector passes.

    .. image:: images/refraction_3d_setup.png

    The rendered result should should look roughly like this (IOR ``1.0`` and ``1.5``):

    .. image:: images/refraction_vector10.png
        :width: 300 px
    .. image:: images/refraction_vector15.png
        :width: 300 px

    From this the gizmo will calculate a Refraction/IOR mask that is the basis of the effect. The mask can be previewed by toggling the ``Preview Mask`` switch in the UI:

    .. image:: images/refraction_mask.png

    Adjusting the parameters described below will yield results similar to the effect example image at the the end of this section. The effect can be previewed by toggling the ``Preview Effect`` switch in the UI.

    .. image:: images/refraction_diffusion.png


    Channels:

    :param Refraction_RGB: Refraction RGB pass, default: ``VRayRefraction``
    :type Refraction_RGB: str
    :param Low_IOR: Refraction vector pass with lower IOR value, default: ``RefractionVector10``
    :type Low_IOR: str
    :param High_IOR: Refraction vector pass with higher IOR value, default: ``RefractionVector15``
    :type High_IOR: str

    IOR Mask:

    :param Preview_Mask: Display the IOR/refraction mask only, default: ``False``
    :type Preview_Mask: bool
    :param Gain: IOR/refraction mask multiplier, default: ``1.8``
    :type Gain: float
    :param Gamma: IOR/refraction mask gamma, default: ``0.35``
    :type Gamma: float
    :param Blur: IOR/refraction mask overall blur in pixels, default: ``2.5``
    :type Blur: float

    Diffusion:

    :param Preview_Effect: Display the effect only, default: ``False``
    :type Preview_Effect: bool
    :param Amount: Overall strength of the effect, i.e. separation of RGB channels, default: ``1.0``
    :type Amount: float
    :param Blur: Effect RGB blur in pixels, default: ``5.0``
    :type Blur: float
    :param Gain: Effect RGB multiplier, default: ``0.5``
    :type Gain: float
    :param Gamma: Effect RGB gamma, default: ``1.5``
    :type Gamma: float
    :param Saturation: Effect RGB saturation, default: ``2.0``
    :type Saturation: float
    :param Mix: Effect mix or opacity value, default: ``1.0``
    :type Mix: float

    Advanced > Blur Weights:

    :param Blur_R: Relative strength of the effect blur on the R channel, default: ``1.0``
    :type Blur_R: float
    :param Blur_G: Relative strength of the effect blur on the G channel, default: ``2.0``
    :type Blur_G: float
    :param Blur_B: Relative strength of the effect blur on the B channel, default: ``3.0``
    :type Blur_B: float

    Advanced > Diffusion Weights:

    :param Diffusion_R: Relative strength of the effect on the R channel, default: ``1.25``
    :type Diffusion_R: float
    :param Diffusion_G: Relative strength of the effect on the G channel, default: ``1.0``
    :type Diffusion_G: float
    :param Diffusion_B: Relative strength of the effect on the B channel, default: ``1.5``
    :type Diffusion_B: float


    Effect example:

    .. image:: images/refraction_result.png



V-Ray Tonemapper
----------------

.. py:function:: vray_tonemapper

    This gizmo implements the V-Ray ``Reinhard`` and ``Exponential`` tone mappers. `Documentation <https://docs.chaosgroup.com/display/VRAY3MAYA/Color+Mapping>`_.

    .. image:: images/vray_tonemapper.png


    Global:

    :param Tonemapper: Tone mapping algorithm to be used
    :type Tonemapper: str

    Reinhard:

    :param Multiplier: The overall multiplier when the ``Tonemapper`` is set to ``Reinhard``.
    :type Multiplier: float
    :param Burn: Adjusts the blend of mapping between linear and exponential style for the ``Reinhard`` tone mapper. If Burn Value is ``1.0``, the result is linear color mapping; if Burn Value is ``0.0``, the result is exponential-style mapping.
    :type Burn: float

    Exponential:

    :param Dark_Multiplier: The multiplier for dark colors.
    :type Dark_Multiplier: float
    :param Bright_Multiplier: The multiplier for bright colors.
    :type Bright_Multiplier: float
