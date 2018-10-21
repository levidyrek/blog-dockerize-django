var $referralFields = $( ".referral-fields" );

// Hide/show referral fields based on the user's selection.
$( "#id_is_referral" ).change( function() {
    if ( $( this ).is( ":checked" ) ) {
        $referralFields.removeClass( "hidden" );
    } else {
        $referralFields.addClass( "hidden" );
    }
} ).change();  // Trigger an initial change() to set the initial state.

// Set up validation on the form, ignoring hidden fields.
$( "#application-form" ).validate( {
    ignore: "input:not(:visible)"
} );
